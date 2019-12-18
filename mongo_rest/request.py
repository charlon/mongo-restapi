spot = Spot.objects.create(
    name="My Cool Spot",
    location={ type: "Point", coordinates: [-73.856077, 40.848447] },
    hours=[SpotAvailableHours(day="monday", start_time="10am", end_time="11pm"])
)
