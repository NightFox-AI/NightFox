# NightFox
NightFox is an AI capable of playing simple state based games without using Artificial neural networks and only on primitive AI algorithms . 

## Installation
* Install the dependencies and clone the project.
```
$ pip3 install ga2
$ git clone https://github.com/NightFox-AI/NightFox
```
## Usage
 #### Training process 
 (Optional, the trained dna file is already included) :
* Set the required parameters in the [gamecontrol.py](https://github.com/NightFox-AI/NightFox/blob/master/gamecontrol.py) file .
		``` $ python3 gamecontrol.py```
*  Stat of the training process is shown while training goes on .

#### Playing with the agent
* Currently the replay option is shown but is not functional, please 
re-run the python file to play.
	``` $ python gui.py ```
* To increase/decrease difficulty level, modify the **_pd_** parameter in  [gui.py](https://github.com/NightFox-AI/NightFox/blob/master/gui.py) python file.

## Contributions
* Kind souls may send a Pull request with appropriate Bug fix/ New feature . Constructive contributions are appreciated.