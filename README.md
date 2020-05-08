# rex-gym Environment for Multiple behaviors 

Modified reward function 

extended observation vector

in particular :

in _init_() function, initialized:

```
self.affordance = [-1,-1,-1,-1,-1] 
self.model ='Stand'
```

in step function I added the following lines: 


```
if self._env_step_counter >0 and self._env_step_counter%200 ==0:
  model_index = random.randint(0,2)
  self.affordance = np.dot([1,1,1,1,1],model_index)
  self._model = Behavioral_models[model_index]
  ```
  
 As the dictionary ```Behavioral_models``` defined as: 
 
 ```
 Behavioral_models  = {-1:'Stand',
                    0:'Walk',
                    1:'Gallop',
                    2:'Turn'}
 ```
 
  In observation function I extended the observation pattern with :
  
  ```
  observation.extend(self.affordance)
  ```
