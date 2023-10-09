#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Define the hypothesized cumulative distribution function F0(x)
double F0(double x) {
    if (x < 0) {
        return 0;
    } else if (x >= 0 && x < 1) {
        return x;
    } else {
        return 1;
    }
}

int main() {
    // Given data
    double data[] = {0.13, 0.12, 0.78, 0.51};
    int n = sizeof(data) / sizeof(data[0]);

    // Sort the data in ascending order
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (data[i] > data[j]) {
                double temp = data[i];
                data[i] = data[j];
                data[j] = temp;
            }
        }
    }

    // Calculate the EDF (Empirical Distribution Function) values
    double edf_values[n];
    for (int i = 0; i < n; i++) {
        edf_values[i] = (i + 1) / (double)n;
    }

    // Calculate the absolute differences between EDF and F0
    double differences[n];
    for (int i = 0; i < n; i++) {
        differences[i] = fabs(edf_values[i] - F0(data[i]));
    }

    // Find the maximum absolute difference (Kolmogorov-Smirnov test statistic D)
    double D = 0;
    for (int i = 0; i < n; i++) {
        if (differences[i] > D) {
            D = differences[i];
        }
    }

    // Given significance level and critical value
    double alpha = 0.01;
    double critical_value = 0.669;

    // Perform the hypothesis test
    int psi = (D <= critical_value) ? 1 : 0;

    // Calculate the observed value of D + ψ
    double observed_value = D + psi;

    // Print the results
    printf("Kolmogorov-Smirnov test statistic D: %lf\n", D);
    printf("ψ: %d\n", psi);
    printf("Observed value of D + ψ: %lf\n", observed_value);

    return 0;
}

