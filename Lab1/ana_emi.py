import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

# Load and parse the XML emissions file
def parse_emissions(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    emission_data = []

    for timestep in root.findall('timestep'):
        time = float(timestep.attrib['time'])
        for vehicle in timestep.findall('vehicle'):
            emission_data.append({
                'time': time,
                'vehicle_id': vehicle.attrib['id'],
                'CO2': float(vehicle.attrib.get('CO2', 0)),
                'CO': float(vehicle.attrib.get('CO', 0)),
                'HC': float(vehicle.attrib.get('HC', 0)),
                'NOx': float(vehicle.attrib.get('NOx', 0)),
                'PMx': float(vehicle.attrib.get('PMx', 0)),
                'fuel': float(vehicle.attrib.get('fuel', 0))
            })

    emission_df = pd.DataFrame(emission_data)
    return emission_df

# Plot the emission data
def plot_emissions(emission_df):
    plt.figure(figsize=(12, 10))

    # Plot CO2 Emissions over Time
    plt.subplot(3, 1, 1)
    plt.plot(emission_df['time'].values, emission_df['CO2'].values, label='CO2 Emissions', color='g')
    plt.xlabel('Time (s)')
    plt.ylabel('CO2 Emissions (g)')
    plt.title('CO2 Emissions Over Time')
    plt.legend()
    plt.grid(True)

    # Plot Fuel Consumption over Time
    plt.subplot(3, 1, 2)
    plt.plot(emission_df['time'].values, emission_df['fuel'].values, label='Fuel Consumption', color='orange')
    plt.xlabel('Time (s)')
    plt.ylabel('Fuel Consumption (ml)')
    plt.title('Fuel Consumption Over Time')
    plt.legend()
    plt.grid(True)

    # Plot NOx Emissions over Time
    plt.subplot(3, 1, 3)
    plt.plot(emission_df['time'].values, emission_df['NOx'].values, label='NOx Emissions', color='r')
    plt.xlabel('Time (s)')
    plt.ylabel('NOx Emissions (g)')
    plt.title('NOx Emissions Over Time')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('2.3emi.jpg')
    plt.show()

# Main function to run the analysis and plotting
def main():
    # File path for the emissions XML file
    emissions_file = 'emissions.xml'

    # Parse and analyze the emissions file
    emission_df = parse_emissions(emissions_file)

    # Plot the results
    plot_emissions(emission_df)

if __name__ == "__main__":
    main()
