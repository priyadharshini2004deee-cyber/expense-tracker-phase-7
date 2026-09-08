from flask import Flask, render_template, request, jsonify
from pathlib import Path
from datetime import datetime
import json, uuid

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "database" / "data.json"
app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

def load():
    if not DB.exists():
        save({"users":[],"expenses":[]})
    try:
        return json.loads(DB.read_text(encoding="utf-8"))
    except Exception:
        return {"users":[],"expenses":[]}

def save(data):
    tmp = DB.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(DB)

def user(data, uid):
    return next((u for u in data["users"] if u["id"] == uid), None)

def norm(v):
    return " ".join(str(v or "").strip().split())

def amount(v):
    raw = str(v or "").strip()
    if not raw: return None, "Please enter an amount."
    try: n = float(raw)
    except ValueError: return None, "Amount must be a valid number."
    if n <= 0: return None, "Amount must be greater than zero."
    return round(n,2), None

def date_value(v):
    raw = str(v or "").strip()
    if not raw: return None, "Please select a date."
    try:
        d = datetime.strptime(raw, "%Y-%m-%d").date()
    except ValueError:
        return None, "Please enter a valid date."
    return d.isoformat(), None

def text_required(v, label):
    x = norm(v)
    return (x, None) if x else (None, f"Please enter a {label}.")

def valid_expenses(data, uid):
    out=[]
    for e in data["expenses"]:
        if e.get("user_id") != uid: continue
        try:
            n=float(e["amount"]); datetime.strptime(e["date"], "%Y-%m-%d")
            if n <= 0 or not norm(e.get("category")) or not norm(e.get("description")): continue
            out.append(e)
        except Exception: continue
    return out

@app.get("/")
def index(): return render_template("index.html")

@app.get("/api/state")
def state(): return jsonify(load())

@app.post("/api/users")
def create_user():
    data=load(); p=request.get_json(silent=True) or {}; name=norm(p.get("name"))
    if not name: return jsonify(ok=False,message="Please enter a user name."),400
    if any(norm(u["name"]).casefold()==name.casefold() for u in data["users"]):
        return jsonify(ok=False,message="A user with this name already exists."),409
    u={"id":uuid.uuid4().hex,"name":name}; data["users"].append(u); save(data)
    return jsonify(ok=True,user=u),201

@app.post("/api/expenses")
def create_expense():
    data=load(); p=request.get_json(silent=True) or {}; uid=str(p.get("user_id") or "")
    if not user(data,uid): return jsonify(ok=False,message="Please select a valid active user."),400
    a,e=amount(p.get("amount"))
    if e:return jsonify(ok=False,message=e),400
    d,e=date_value(p.get("date"))
    if e:return jsonify(ok=False,message=e),400
    c,e=text_required(p.get("category"),"category")
    if e:return jsonify(ok=False,message=e),400
    desc,e=text_required(p.get("description"),"description")
    if e:return jsonify(ok=False,message=e),400
    now=datetime.utcnow().isoformat(timespec="seconds")+"Z"
    x={"id":uuid.uuid4().hex,"user_id":uid,"amount":a,"date":d,"category":c,"description":desc,"created_at":now,"updated_at":now}
    data["expenses"].append(x); save(data); return jsonify(ok=True,expense=x),201

def owned(data,eid,uid): return next((x for x in data["expenses"] if x["id"]==eid and x["user_id"]==uid),None)

@app.put("/api/expenses/<eid>")
def update(eid):
    data=load(); p=request.get_json(silent=True) or {}; uid=str(p.get("user_id") or "")
    if not user(data,uid): return jsonify(ok=False,message="Please select a valid active user."),400
    x=owned(data,eid,uid)
    if not x: return jsonify(ok=False,message="The selected expense could not be found for the active user."),404
    a,e=amount(p.get("amount"))
    if e:return jsonify(ok=False,message=e),400
    d,e=date_value(p.get("date"))
    if e:return jsonify(ok=False,message=e),400
    c,e=text_required(p.get("category"),"category")
    if e:return jsonify(ok=False,message=e),400
    desc,e=text_required(p.get("description"),"description")
    if e:return jsonify(ok=False,message=e),400
    x.update(amount=a,date=d,category=c,description=desc,updated_at=datetime.utcnow().isoformat(timespec="seconds")+"Z")
    save(data); return jsonify(ok=True,expense=x)

@app.delete("/api/expenses/<eid>")
def delete(eid):
    data=load(); p=request.get_json(silent=True) or {}; uid=str(p.get("user_id") or "")
    if not user(data,uid): return jsonify(ok=False,message="Please select a valid active user."),400
    x=owned(data,eid,uid)
    if not x:return jsonify(ok=False,message="The selected expense could not be found for the active user."),404
    data["expenses"]=[e for e in data["expenses"] if e["id"]!=eid]; save(data)
    return jsonify(ok=True)

@app.get("/api/dashboard/<uid>")
def dashboard(uid):
    data=load()
    if not user(data,uid): return jsonify(ok=False,message="Invalid active user."),400
    xs=valid_expenses(data,uid); total=round(sum(float(x["amount"]) for x in xs),2); count=len(xs)
    avg=round(total/count,2) if count else 0
    breakdown={}
    for x in xs: breakdown[x["category"]]=round(breakdown.get(x["category"],0)+float(x["amount"]),2)
    return jsonify(ok=True,total=total,average=avg,count=count,breakdown=breakdown,expenses=xs)

if __name__=="__main__":
    load(); app.run(host="127.0.0.1",port=5000,debug=False)
