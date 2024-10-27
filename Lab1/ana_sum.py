import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

# Load and parse the XML summary file
def parse_summary(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    summary_data = []

    for step in root.findall('step'):
        summary_data.append({
            'time': float(step.attrib['time']),
            'running': int(step.attrib['running']),
            'meanWaitingTime': float(step.attrib['meanWaitingTime']),
            'meanSpeed': float(step.attrib['meanSpeed'])
        })

    summary_df = pd.DataFrame(summary_data)
    return summary_df

# Plot the data
def plot_summary(summary_df):
    plt.figure(figsize=(12, 8))

    # Plot Running Vehicles
    plt.subplot(3, 1, 1)
    plt.plot(summary_df['time'].values, summary_df['running'].values, label='Running Vehicles', color='b')
    plt.xlabel('Time (s)')
    plt.ylabel('Running Vehicles')
    plt.title('Number of Running Vehicles Over Time')
    plt.legend()
    plt.grid(True)

    # Plot Mean Waiting Time
    plt.subplot(3, 1, 2)
    plt.plot(summary_df['time'].values, summary_df['meanWaitingTime'].values, label='Mean Waiting Time', color='g')
    plt.xlabel('Time (s)')
    plt.ylabel('Mean Waiting Time (s)')
    plt.title('Mean Waiting Time Over Time')
    plt.legend()
    plt.grid(True)

    # Plot Mean Speed
    plt.subplot(3, 1, 3)
    plt.plot(summary_df['time'].values, summary_df['meanSpeed'].values, label='Mean Speed', color='r')
    plt.xlabel('Time (s)')
    plt.ylabel('Mean Speed (m/s)')
    plt.title('Mean Speed Over Time')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('2.3_sum.jpg')
    plt.show()

# Main function to run the analysis and plotting
def main():
    # File path for the summary XML file
    summary_file = 'summary.xml'

    # Parse and analyze the summary file
    summary_df = parse_summary(summary_file)

    # Plot the results
    plot_summary(summary_df)

if __name__ == "__main__":
    main()