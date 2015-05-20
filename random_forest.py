import numpy as np
from sklearn.ensemble import RandomForestRegressor

validation_path = "validation/features/"

features_path = "training/features/"
features = []
features.append( "checkmate_move_done")
features.append( "is_draw")
features.append( "last_scores")
features.append( "match_len")
features.append( "mean")
features.append( "no_of_checks_scaled")
features.append( "no_of_mistakes_scaled")
features.append( "no_of_piece_taken_scaled")
features.append( "std_points")

labels_path = "training/labels/sum.lab"

feature_list = []
for feature in features:
	feature_list.append( np.loadtxt( features_path + feature + ".fea"))

X = np.asarray( feature_list[0])

for i in xrange(1, len(feature_list)):
	X = np.column_stack( (X, feature_list[i]))

Y = np.loadtxt( labels_path)

regressor = RandomForestRegressor(n_estimators=10)
regressor.fit(X,Y)

training_result = regressor.predict(X)
np.savetxt( "results/rf_training_1", training_result, fmt='%.1f')

#Feature Importance

for i in xrange( len(features)):
	print features[i] + " -> " + str( regressor.feature_importances_[i])

#Validation Data
feature_list = []
for feature in features:
	feature_list.append( np.loadtxt( validation_path + feature + ".fea"))

X = np.asarray( feature_list[0])

for i in xrange(1, len(feature_list)):
	X = np.column_stack( (X, feature_list[i]))

validation_result = regressor.predict(X)
np.savetxt( "results/rf_validation_1", validation_result, fmt='%.1f')
