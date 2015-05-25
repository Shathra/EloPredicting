#!/usr/bin/python

import numpy as np
from tester import test
from sklearn.ensemble import RandomForestRegressor

validation_path = "validation/features/"
features_path = "training/features/"
labels_path = "training/labels/sum.lab"

results_path = "testing/"

features = []
#features.append( "checkmate_move_done")
#features.append( "is_draw")
features.append( "last_scores")
features.append( "match_len")
features.append( "mean")
features.append( "no_of_checks_scaled")
features.append( "no_of_mistakes_scaled")
features.append( "no_of_piece_taken_scaled")
features.append( "std_points")

feature_list = []
for feature in features:
	feature_list.append( np.loadtxt( features_path + feature + ".fea"))

X = np.asarray( feature_list[0])

for i in xrange(1, len(feature_list)):
	X = np.column_stack( (X, feature_list[i]))

Y = np.loadtxt( labels_path)

regressor = RandomForestRegressor(n_estimators=20)
regressor.fit(X,Y)

training_result = regressor.predict(X)
np.savetxt( results_path + "training", training_result, fmt='%.1f')

#Validation Data
feature_list = []
for feature in features:
	feature_list.append( np.loadtxt( validation_path + feature + ".fea"))

X = np.asarray( feature_list[0])

for i in xrange(1, len(feature_list)):
	X = np.column_stack( (X, feature_list[i]))

validation_result = regressor.predict(X)
np.savetxt( results_path + "validation", validation_result, fmt='%.1f')

#Errors

training_err = test( labels_path, results_path + "training")
validation_err = test( "validation/labels/sum.lab", results_path + "validation")

print "Training Error"
print training_err

print "Validation Error"
print validation_err

#Feature Importance

for i in xrange( len(features)):
	print features[i] + " -> " + str( regressor.feature_importances_[i])