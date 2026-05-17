from flask import Flask, render_template

app = Flask(__name__)

# ---------- Data ----------

GYM_DATA = {
    "name": "IRONFORGE GYM",
    "tagline": "Forge Your Limits",
    "founded": 2015,
    "members": 1200,
    "trainers": 18,
    "highlights": [
        {"icon": "🏋️", "title": "Olympic Lifting", "desc": "Professional-grade platforms and barbells for serious lifters."},
        {"icon": "🔥", "title": "HIIT Studio", "desc": "High-intensity classes that torch calories and build endurance."},
        {"icon": "🧘", "title": "Recovery Zone", "desc": "Sauna, cold plunge, and stretching area for optimal recovery."},
        {"icon": "🥊", "title": "Boxing Ring", "desc": "Full-size ring with bags, speed balls, and gloves provided."},
    ],
    "team": [
        {"name": "Marcus Cole", "role": "Head Coach & Founder", "cert": "NSCA-CSCS, 15 yrs exp", "emoji": "💪"},
        {"name": "Priya Sharma", "role": "Nutrition & Wellness", "cert": "Registered Dietitian", "emoji": "🥗"},
        {"name": "Jake Torres", "role": "HIIT & Cardio Lead", "cert": "ACE Certified, 8 yrs exp", "emoji": "⚡"},
        {"name": "Leila Hassan", "role": "Yoga & Recovery", "cert": "RYT-500, Mobility Specialist", "emoji": "🧘"},
    ],
    "facilities": [
        {"name": "Free Weights Floor", "detail": "15,000 sq ft of free weights, racks, and platforms"},
        {"name": "Cardio Deck", "detail": "80+ machines — treadmills, rowers, assault bikes"},
        {"name": "Group Class Studio", "detail": "Sprung floor, sound system, live DJ nights"},
        {"name": "Recovery Suite", "detail": "Infrared sauna, ice bath, compression therapy"},
        {"name": "Juice & Protein Bar", "detail": "In-house nutrition bar with supplements"},
        {"name": "Secure Lockers", "detail": "Digital lockers, towel service, private showers"},
    ],
    "plans": [
        {
            "name": "STARTER",
            "price": 29,
            "period": "/ month",
            "color": "var(--bronze)",
            "features": [
                "Gym floor access (6am–10pm)",
                "2 group classes / week",
                "Locker & shower access",
                "Mobile app tracking",
            ],
            "highlight": False,
        },
        {
            "name": "PRO",
            "price": 59,
            "period": "/ month",
            "color": "var(--accent)",
            "features": [
                "24/7 gym access",
                "Unlimited group classes",
                "1 PT session / month",
                "Nutrition consultation",
                "Recovery suite access",
                "Guest passes (2/mo)",
            ],
            "highlight": True,
        },
        {
            "name": "ELITE",
            "price": 99,
            "period": "/ month",
            "color": "var(--silver)",
            "features": [
                "Everything in PRO",
                "4 PT sessions / month",
                "Custom meal plan",
                "Priority class booking",
                "Unlimited guest passes",
                "Quarterly body scan",
            ],
            "highlight": False,
        },
    ],
}


# ---------- Routes ----------

@app.route("/")
def home():
    return render_template("home.html", gym=GYM_DATA)


@app.route("/about")
def about():
    return render_template("about.html", gym=GYM_DATA)


@app.route("/membership")
def membership():
    return render_template("membership.html", gym=GYM_DATA)


if __name__ == "__main__":
    app.run(debug=True)
