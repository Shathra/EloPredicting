#!/usr/bin/python

import numpy as np
from tester import test
from sklearn.ensemble import RandomForestRegressor

test_path = "test/features/"
features_path = "training/features/"
labels_path = "training/labels/"

features = []
features.append( "last_scores")
features.append( "match_len")
features.append( "mean")
features.append( "no_of_checks_scaled")
features.append( "no_of_mistakes_scaled")
features.append( "no_of_piece_taken_scaled")
features.append( "std_points")
features.append( "castle")
features.append( "queen")
features.append( "score_dif")

feature_list = []
for feature in features:
	feature_list.append( np.loadtxt( features_path + feature + ".fea"))

X = np.asarray( feature_list[0])

for i in xrange(1, len(feature_list)):
	X = np.column_stack( (X, feature_list[i]))

Y = np.loadtxt( labels_path + "sum.lab")

regressor = RandomForestRegressor(n_estimators=20)
regressor.fit(X,Y)

print( "...A+B predictor is ready")

#Test Data A+B
feature_list = []
for feature in features:
	feature_list.append( np.loadtxt( test_path + feature + ".fea"))

X = np.asarray( feature_list[0])

for i in xrange(1, len(feature_list)):
	X = np.column_stack( (X, feature_list[i]))

test_result_sum = regressor.predict(X)

print( "...A+B labels are predicted")
#A-B

features = []
features.append( "last_scores")
features.append( "match_len")
features.append( "mean")
features.append( "max_black")
features.append( "max_white")
features.append( "min_black")
features.append( "min_white")
features.append( "no_of_black_mistakes_scaled")
features.append( "no_of_white_mistakes_scaled")
features.append( "no_of_piece_taken_scaled")
features.append( "std_points")
features.append( "castle_black")
features.append( "castle_white")
features.append( "queen_black")
features.append( "queen_white")
features.append( "score_dif")

feature_list = []
for feature in features:
	feature_list.append( np.loadtxt( features_path + feature + ".fea"))

X = np.asarray( feature_list[0])

for i in xrange(1, len(feature_list)):
	X = np.column_stack( (X, feature_list[i]))

Y = np.loadtxt( labels_path + "dif.lab")

regressor = RandomForestRegressor(n_estimators=20)
regressor.fit(X,Y)

print( "...A-B predictor is ready")

#Test Data A+B
feature_list = []
for feature in features:
	feature_list.append( np.loadtxt( test_path + feature + ".fea"))

X = np.asarray( feature_list[0])

for i in xrange(1, len(feature_list)):
	X = np.column_stack( (X, feature_list[i]))

test_result_dif = regressor.predict(X)
print( "...A-B labels are predicted")
print( "\n...Generating submission file")

final_fd = open( "submission.csv", "w")
final_fd.write( "Event,WhiteElo,BlackElo\n")

for i in xrange( len(test_result_sum)):

	white = test_result_sum[i] + test_result_dif[i]
	white = int( white / 2)

	black = test_result_sum[i] - test_result_dif[i]
	black = int( black / 2)

	final_fd.write( str(25001 + i) + "," + str(white) + "," + str(black) + "\n")

final_fd.close()

print '\033[92m' + '\nSubmission file is generated (submission.csv)' + '\033[0m'