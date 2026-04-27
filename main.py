import pandas as pd
import matplotlib.pyplot as plt

def remove_outliers(data, min_value=40, max_value=180):
    return data[(data["heart_rate"] >= min_value) & (data["heart_rate"] <= max_value)]

def moving_average(data, window_size=5):
    data = data.copy()
    data["filtered_heart_rate"] = data["heart_rate"].rolling(window=window_size).mean()
    return data

def main():
    data = pd.read_csv("sample_data.csv")

    cleaned_data = remove_outliers(data)
    filtered_data = moving_average(cleaned_data)

    average_hr = filtered_data["filtered_heart_rate"].mean()

    print(f"평균 심박수: {average_hr:.2f} bpm")

    plt.plot(data["time"], data["heart_rate"], label="Original")
    plt.plot(filtered_data["time"], filtered_data["filtered_heart_rate"], label="Filtered")
    plt.xlabel("Time")
    plt.ylabel("Heart Rate")
    plt.legend()
    plt.savefig("result.png")
    plt.show()

if __name__ == "__main__":
    main()