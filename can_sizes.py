from math import pi

def main():
    data = [
        ("#1 Picnic", 6.83, 10.16, 0.28), 
        ("#1 Tall", 7.78, 11.91, 0.43), 
        ("#2", 8.73, 11.59, 0.45), 
        ("#2.5", 10.32, 11.91, 0.61), 
        ("#3 Cylinder", 10.79, 17.78, 0.86), 
        ("#5", 13.02, 14.29, 0.83), 
        ("#6Z", 5.40, 8.89, 0.22), 
        ("#8Z short", 6.83, 7.62, 0.26), 
        ("#10", 15.72, 17.78, 1.53), 
        ("#211", 6.83, 12.38, 0.34), 
        ("#300", 7.62, 11.27, 0.38), 
        ("#303", 8.10, 11.11, 0.42)
    ]

    highest_storage_eff = 0
    highest_cost_eff = 0
    highest_storage_eff_name = ""
    highest_cost_eff_name = ""

    for name, radius, height, cost in data:
        volume = cylinder_volume(radius, height)
        surface_area = cylinder_surface_area(radius, height)

        storage = storage_efficiency(volume, surface_area)
        cost_eff = cost_efficiency(volume, cost)
        print(f"{name} - Storage: {storage:.1f}, Cost Efficiency: {cost_eff:.0f}")

        if highest_storage_eff < storage:
            highest_storage_eff = storage
            highest_storage_eff_name = name
        if highest_cost_eff < cost_eff:
            highest_cost_eff = cost_eff
            highest_cost_eff_name = name
    
    print(f"Highest Storage Efficiency: '{highest_storage_eff_name}' with {highest_storage_eff:.1f}")
    print(f"Highest Cost Efficiency: '{highest_cost_eff_name}' with {highest_cost_eff:.0f}")

def storage_efficiency(volume, surface_area):
    storage_eff = volume / surface_area
    return storage_eff

def cost_efficiency(volume, cost):
    cost_eff = volume / cost
    return cost_eff

def cylinder_volume(radius, height):
    volume = pi * radius ** 2 * height
    return volume

def cylinder_surface_area(radius, height):
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area

main()