# rex-gym Environment for Multiple behaviors 

Modified reward function 

extended observation vector

in particular :

## in _init_() function, initialized:

```
self.affordance = [-1,-1,-1,-1,-1] 
self.model ='Stand'
self.reference_base_position = []
self.target_orientation = []
```

## in step function I added the following lines: 


```
if self._env_step_counter >0 and self._env_step_counter%200 ==0:
            
            model_index = random.randint(0,3)
            self.affordance = np.dot([1,1,1,1,1],model_index)

            self.model = Behavioral_models[model_index]
            print(self.model)

            if self.model =='Turn Right' or self.model=='Turn Left': 
                
                self.reference_base_position = self.rex.GetBasePosition()
                
                if self.model == 'Turn Right':
                    target_angle =  random.uniform(-math.pi/4, -math.pi/2)
                    cur_orient = self.pybullet_client.getEulerFromQuaternion(self.rex.GetBaseOrientation())
                    self.target_orientation = [0,0,cur_orient[2]+target_angle]
                    
                elif self.model =='Turn Left':
                    target_angle =  random.uniform(math.pi/4, math.pi/2)
                    cur_orient = self.pybullet_client.getEulerFromQuaternion(self.rex.GetBaseOrientation())
                    self.target_orientation = [0,0,cur_orient[2]+target_angle]
  ```
  
 As the dictionary ```Behavioral_models``` defined as: 
 
 ```
 Behavioral_models  = {-1:'Stand',
                    0:'Walk',
                    1:'Gallop',
                    2:'Turn Right',
                    3:'Turn Left'}
 ```
 
  ## In observation function I extended the observation pattern with :
  
  ```
  observation.extend(self.affordance)
  ```

## Modified Termination condition:
```
def _termination(self):
        position = self.rex.GetBasePosition()
        
        o = self.rex.GetBaseOrientation()
        
        
        if self.model == 'Stand':
            roll, pitch, _ = self.rex.GetTrueBaseRollPitchYaw()
            return math.fabs(roll) > 0.3 or math.fabs(pitch) > 0.5
        
        else:
            if position[2] < 0.13:
                print("IS FALLEN!")
            
            if self.is_fallen():
                print("IS ROTATING!")
         
            return self.is_fallen() or position[2] < 0.13
```
