#include <iostream>
#include <vector>
#include <Eigen/Dense>

using namespace Eigen;
using namespace std;

double calculateError(const VectorXd& h, const VectorXd& t, const VectorXd& coefficients) {
    double error = 0.0;
    for (int i = 0; i < h.size(); ++i) {
        double interpolatedValue = 0.0;
        for (int j = 0; j < coefficients.size(); ++j) {
            interpolatedValue += coefficients[j] * pow(h[i], j);
        }
        error += pow(interpolatedValue - t[i], 2);
    }
    return error;
}

void printPolynomial(const VectorXd& coefficients) {
    cout << "Polynomial: ";
    for (int i = 0; i < coefficients.size(); ++i) {
        cout << coefficients[i];
        if (i < coefficients.size() - 1) {
            cout << " * x^" << i << " + ";
        }
    }
    cout << endl;
}

int main() {
    vector<double> h = {0, 0.2, 0.5, 1, 2, 3, 5, 10, 15, 30, 50, 100, 120};
    vector<double> t = {15, 13.7, 11.8, 8.5, 2, -4.5, 17.5, -49.9, -56.5, -46.6, -2.5, -76.6, 61.3};

    int maxOrder = 10;  // Максимальный порядок полинома для тестирования

    for (int order = 1; order <= maxOrder; ++order) {
        MatrixXd A(h.size(), order + 1);
        VectorXd b(h.size());

        for (int i = 0; i < h.size(); ++i) {
            for (int j = 0; j <= order; ++j) {
                A(i, j) = pow(h[i], j);
            }
            b(i) = t[i];
        }

        VectorXd x = A.jacobiSvd(ComputeThinU | ComputeThinV).solve(b);
        double error = calculateError(Map<VectorXd>(h.data(), h.size()), Map<VectorXd>(t.data(), t.size()), x);

        cout << "Order: " << order << ", Error: " << error << endl;
        printPolynomial(x);
        cout << endl;
    }

    return 0;
}
