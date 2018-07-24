#!/usr/bin/env python2
# -*- coding: utf-8 -*-

if __name__ == '__main__' :
	from os import listdir
	from os.path import isfile, join
	onlyfiles = [f for f in listdir('/data/conda/recnn/data/npyfiles/') if isfile(join('/data/conda/recnn/data/npyfiles/', f))]
	import numpy as np
	import sys
	for i in onlyfiles :
		if i[0]=='B' and not 'merged' in i :
			X1,y1=np.load('/data/conda/recnn/data/npyfiles/'+i)
			X2,y2=np.load('/data/conda/recnn/data/npyfiles/'+'Signal'+i[10:])
			X,y=np.concatenate((X1,X2)),np.concatenate((y1,y2))
			np.save('/data/conda/recnn/data/npyfiles/merged_'+i[11:-4]+'.npy',np.array([X,y]))
