from flask import Flask, jsonify, render_template

app = Flask(__name__)

# ================= API =================
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


if __name__ == "__main__":
    app.run(debug=True)