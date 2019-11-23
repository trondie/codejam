#pragma once
#include "matrix.h"

#include <iostream>
#include <vector>
#include <set>
#include <queue>

using namespace std;

typedef Vector3<int> Point;

const int ROTATION_SYMMETRY = 4;
const int LEFT_ROTATION_SYMMETRY = 2;
const int RIGHT_ROTATION_SYMMETRY = 2;
const int SYMMETRY_PERMUTATION = 12;

// test to see if (xp, yp) is on linesegment between (x1,y1) and (x2,y2)
// - given that the crossproduct is 0.
// The containment point is hardcoded . 
bool checkOnBorder(Point & p1, Point & p2) {
	return (min(p1.at(0), p2.at(0)) <= 0
		&& 0 <= max(p1.at(0), p2.at(0))
		&& min(p1.at(1), p2.at(1)) <= 0
		&& 0 <= max(p1.at(1), p2.at(1)));
}

long long countTriangles(int radius) {

	vector<Point> points;

	// Generate lattice / points
	for (int x = -radius + 1; x < radius; x++) {
		for (int y = -radius + 1; y < radius; y++) {
			if (x == 0 && y == 0) continue;
			if (x*x + y*y < radius * radius) {
				points.push_back(Point(x, y, 0));
			}
		}
	}
	long long sum = 0;
	for (int i = 0; i < points.size(); ++i) {
		int leftBound = 0;
		int rightBound = 0;
		int onBorder = 0;
		int outsideBorder = 0;
		for (int j = 0; j < points.size(); ++j) {
			if (i == j) {
				continue;
			}
			// The direction is illustrated from the z component (after xprod).
			int direction = points[i].crossProduct(points[j]).at(2);
			// The direction shows if the line is leftbound or rightbound w.r.t the origin
			// r.h rule. 
			if (direction < 0) leftBound++;
			if (direction > 0) rightBound++;
			if (direction == 0) {
				if (checkOnBorder(points[i], points[j])) { onBorder++; }
				else { outsideBorder++; }
			}
		}
		// Add and subtract for the new lines. 
		sum += (leftBound * rightBound) * ROTATION_SYMMETRY;
		sum += (leftBound + rightBound) * outsideBorder;
		sum -= (leftBound + rightBound) * onBorder * 2;
		sum -= (leftBound - 1) * leftBound;
		sum -= (rightBound - 1) * rightBound;
	}
	return sum / SYMMETRY_PERMUTATION;
}