from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# ================= DUMMY VIP DATA =================
VIP_USERS = {
    123456789: {"vip": True, "plan": "GOLD", "expire": "2026-03-01"},
    987654321: {"vip": True, "plan": "SILVER", "expire": "2026-02-15"}
}

# ================= API: VIP STATUS =================
@app.route("/api/vipstatus")
def vip_status():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id missing"}), 400

    try:
        uid = int(user_id)
    except ValueError:
        return jsonify({"error": "invalid user_id"}), 400

    if uid in VIP_USERS:
        return jsonify(VIP_USERS[uid])
    else:
        return jsonify({"vip": False, "plan": None, "expire": None})

# ================= API: SHOP =================
@app.route("/api/shop")
def shop_api():
    return jsonify({
        "shop_name": "REAL VIP SHOP",
        "category": "FF REAL PRODUCTS",

        "paid_products": [
            {"name": "2K Likes", "price": "₹999"},
            {"name": "5K Likes", "price": "₹1500"}
        ],

        "free_products": [
            {"name": "FF MOD MENU", "type": "main"},
            {"name": "FF SAFE METADATA FILE", "type": "main"},
            {"name": "FF LUA FILE", "type": "main"},
            {"name": "FF LIKE GROUP", "type": "like_group"},
            {"name": "JWT TOKEN BOT", "type": "jwt_bot"}
        ],

        "links": {
            "main": "https://t.me/+EpqfTSROwzIwMGJl",
            "like_group": "https://t.me/+kxmchJsseDxjYzhl",
            "jwt_bot": "https://t.me/@JWT_Elite_Generator_BOT"
        },

        "community": {
            "channel": "https://t.me/+EpqfTSROwzIwMGJl",
            "group": "https://t.me/+kxmchJsseDxjYzhl"
        }
    })

# ================= WEBSITE =================
@app.route("/")
def home():
    return render_template("index.html")

# ================= RUN APP =================
if __name__ == "__main__":
    app.run(debug=True)
