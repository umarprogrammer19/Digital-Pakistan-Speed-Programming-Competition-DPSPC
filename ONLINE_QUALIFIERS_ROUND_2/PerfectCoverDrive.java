import java.util.*;

public class PerfectCoverDrive {

    static class Interval {
        double start, end;

        Interval(double s, double e) {
            this.start = s;
            this.end = e;
        }
    }

    static double normalize(double angle) {
        return (angle % 360.0 + 360.0) % 360.0;
    }

    static double perfectCoverDrive(int n, double r, List<double[]> fielders) {
        List<Interval> intervals = new ArrayList<>();

        for (double[] fielder : fielders) {
            double x = fielder[0], y = fielder[1];
            double distance = Math.hypot(x, y);

            if (distance <= r) {
                return 0.000000;
            }

            double centerAngle = Math.toDegrees(Math.atan2(y, x));
            double angleOffset = Math.toDegrees(Math.asin(r / distance));
            double startAngle = normalize(centerAngle - angleOffset);
            double endAngle = normalize(centerAngle + angleOffset);

            if (startAngle > endAngle) {
                intervals.add(new Interval(startAngle, 360.0));
                intervals.add(new Interval(0.0, endAngle));
            } else {
                intervals.add(new Interval(startAngle, endAngle));
            }
        }

        intervals.sort(Comparator.comparingDouble(i -> i.start));

        List<Interval> merged = new ArrayList<>();
        for (Interval interval : intervals) {
            if (merged.isEmpty() || interval.start > merged.get(merged.size() - 1).end) {
                merged.add(new Interval(interval.start, interval.end));
            } else {
                Interval last = merged.get(merged.size() - 1);
                last.end = Math.max(last.end, interval.end);
            }
        }

        double maxGap = 0.0;
        for (int i = 0; i < merged.size(); i++) {
            double end = merged.get(i).end;
            double nextStart = (i == merged.size() - 1)
                    ? merged.get(0).start + 360.0
                    : merged.get(i + 1).start;
            double gap = nextStart - end;
            if (gap > maxGap) {
                maxGap = gap;
            }
        }

        return Math.round(maxGap * 1e6) / 1e6;
    }

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            int n = scanner.nextInt();
            double r = scanner.nextDouble();

            List<double[]> fielders = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                double x = scanner.nextDouble();
                double y = scanner.nextDouble();
                fielders.add(new double[] { x, y });
            }

            double result = perfectCoverDrive(n, r, fielders);
            System.out.printf("%.6f\n", result);
        }
    }
}
