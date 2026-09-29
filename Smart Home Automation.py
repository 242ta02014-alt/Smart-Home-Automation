# Smart Home Automation
# Easy Python Code

print("=== SMART HOME AUTOMATION ===")

light = input("Turn Light ON/OFF: ").lower()
fan = input("Turn Fan ON/OFF: ").lower()
ac = input("Turn AC ON/OFF: ").lower()

print("\n--- HOME STATUS ---")

if light == "on":
    print("Light: ON")
else:
    print("Light: OFF")

if fan == "on":
    print("Fan: ON")
else:
    print("Fan: OFF")

if ac == "on":
    print("AC: ON")
else:
    print("AC: OFF")

print("\nAutomation Complete!")
