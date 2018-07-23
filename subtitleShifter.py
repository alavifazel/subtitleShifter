import argparse
from datetime import datetime, timedelta

parser = argparse.ArgumentParser(description="Shift all subtitle texts by given time")

parser.add_argument("-f", "--filepath", required=True, metavar="", help="Filepath for srt subtitle.")
parser.add_argument("-t", "--time", type=float, required=True, metavar="", help="Time to shift subtitles texts.")
args = parser.parse_args()

def load_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def main():
    outputFile = open(args.filepath[:-4] + "_shiftedBy" + str(args.time) + ".srt", "w")
    lines = load_file(args.filepath)
    for line in lines:
        if line[13:16] == "-->":
            startingTime = line[0:12]
            endingTime = line[17:29]
            dateObj1 = datetime.strptime(startingTime, "%H:%M:%S,%f")
            dateObj2 = datetime.strptime(endingTime, "%H:%M:%S,%f")
            dateObj1 += timedelta(seconds=args.time)
            dateObj2 += timedelta(seconds=args.time)
            outputFile.write(dateObj1.strftime("%H:%M:%S,%f")[:-3] +  " --> " + dateObj2.strftime("%H:%M:%S,%f")[:-3] + "\n")
        else:
            outputFile.write(line)


if __name__ == "__main__":
    main()
