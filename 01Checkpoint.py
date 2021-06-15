age = int(input("Please enter your age: "))

maxHeartRate = 220 - age
exerciseMinHeartRate = .65 * maxHeartRate
exerciseMaxHeartRate = .85 * maxHeartRate

print(f"When you exercise to strengthen your heart, you should\n\
keep your heart rate between {exerciseMinHeartRate:.0f} and {exerciseMaxHeartRate:.0f} beats per minute.")