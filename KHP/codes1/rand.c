#include <stdio.h>
#include <math.h>
#define M_PI 3.14159265358979323846
double cdf(double x) {
    if (x < -1) {
        return 0.5 * (1.0 + erf(x / sqrt(2.0)));
    } 
    else {
        return 0.5 * (1.0 + erf(x+1 / sqrt(2.0)));
    }
}

double pdf(double x) {
    if (x < -1) {
        return 1.0 / (sqrt(2.0 * M_PI)) * exp(-x * x / 2.0);
    } else {
        return 1.0 / (sqrt(2.0 * M_PI)) * exp(-(x + 1) * (x + 1) / 2.0);
    }
}

int main() {
    int num = 10000;
    double x_max = 4.0;
    double x_min = -4.0;
    double step = (x_max - x_min) / num;

    FILE *outfile = fopen("uni.dat", "w");

    for (int i = 0; i < num; i++) {
        double x = x_min + step * i;
        double sample = pdf(x);
        double sample1 = cdf(x);
        fprintf(outfile, "%lf %lf %lf\n", x, sample, sample1);
    }

    fclose(outfile);

    return 0;
}

