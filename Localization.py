# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 16:02:20 2016

@author: Ben
"""
import numpy as np
import random

class Localize(object):
    def __init__(self,x_i,y_i,theta_i,K_x,K_y,K_theta):
        self.x=x_i
        self.y=y_i
        self.theta=theta_i
        self.K_x=K_x
        self.K_y=K_y
        self.K_theta=K_theta
    
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_theta(self):
        return self.theta
    def get_pose(self):
        return self.x,self.y,self.theta
        
    def predict(self,dx,dy,dtheta):
        self.x+=dx
        self.y+=dy
        self.theta+=dtheta
        
        
    def update(self,measured_pose_list):
        x_error_list=[]
        y_error_list=[]
        theta_error_list=[]
        for pose in measured_pose_list:
            x_error_list.append(pose[0]-self.get_x())
            y_error_list.append(pose[1]-self.get_y())
            theta_error_list.append(pose[2]-self.get_theta())
        x_error=np.mean(x_error_list)
        y_error=np.mean(y_error_list)
        theta_error=np.mean(theta_error_list)
        self.x+=self.K_x*x_error
        self.y+=self.K_y*y_error
        self.theta=self.K_theta*theta_error
        
        
        
        
        
#Initialize a localizaiton object with an initial guess for location
        
#When odometry data becomes available, call predict method

#When vision data becomes available, call updata funciton
    #Currently, this takes a list of poses (x,y,theta) of measured robot locaiton in global frame
    #Might want to change it so that it just takes data and does all the transformations internally       
        
        
        
        
        
#t=range(0,10,.01)
#x=np.sin(t)
#y=np.cos(t)
#theta=np.zeros(t.shape)
#
#dx=[]
#dy=[]
#for n in range(len(x)-1):
#    dx.append(x[n+1]-x[n])+.01*np.random.normal()
#    dy.append(y[n+1]-y[n])+.01*np.random.normal()