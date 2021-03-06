import pandas as pd
import matplotlib.pyplot as plt
import calendar


class DataViz():
    def __init__(self):
        pass
    
    def potholes_by_month_viz(self, potholes_df, year):
        # convert the the dates into datetime objects
        potholes_df["SR CREATE DATE"] = pd.to_datetime(potholes_df["SR CREATE DATE"])
        
        # group the dates by month and count the total number of occurences
        counts_series = potholes_df["SR CREATE DATE"]\
            .groupby([potholes_df["SR CREATE DATE"].dt.month])\
            .count()
        
        # change the month numbers to names
        counts_df = counts_series.to_frame()
        counts_df["Month"] = list(counts_series.index)
        counts_df["Month"] = counts_df["Month"].apply(lambda x: calendar.month_abbr[x])
        counts_df.set_index("Month", inplace=True)
        counts_df.rename(columns={"SR CREATE DATE":"Number of Potholes"}, inplace=True)
        
        # plot the visual
        counts_df.plot(kind="bar", legend=False)
        plt.title("Number of Potholes Per Month in " + str(year))
        plt.ylabel("Number of Pothole")
        plt.subplots_adjust(bottom=.2)
        plt.show()
        
    def overdue_by_month_viz(self, potholes_df, year):
        # calculate the average number of overdue days for every month of the year
        potholes_df["SR CREATE DATE"] = pd.to_datetime(potholes_df["SR CREATE DATE"])
        avg_overdue = potholes_df["OVERDUE"].groupby([potholes_df["SR CREATE DATE"].dt.month])
        avg_overdue_series = avg_overdue.mean()

        # change the month numbers to names
        avg_overdue_df = avg_overdue_series.to_frame()
        avg_overdue_df["Month"] = list(avg_overdue_series.index)
        avg_overdue_df["Month"] = avg_overdue_df["Month"].apply(lambda x: calendar.month_abbr[x])
        avg_overdue_df.set_index("Month", inplace=True)
        avg_overdue_df.rename(columns={"SR CREATE DATE": "Average Overdue Days"}, inplace=True)

        # plot the visual
        avg_overdue_df.plot(kind="bar", legend=False)
        plt.axhline()
        plt.title("Average Number of Days Overdue Per Month in " + str(year))
        plt.ylabel("Days")
        plt.subplots_adjust(bottom=.2)
        plt.show()
 
potholes_csv = {
    2019: "../../data/output/potholePiped2019.csv",
    2018: "../../data/output/potholePiped2018.csv",
    2017: "../../data/output/potholePiped2017.csv"
}

if __name__ == "__main__":
    visualizer = DataViz()
    viz_year = 2019
    potholes_df = pd.read_csv(potholes_csv[viz_year])
    # visualizer.potholes_by_month_viz(potholes_df, viz_year)
    visualizer.overdue_by_month_viz(potholes_df, viz_year)