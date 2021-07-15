back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[sphere](models-boussinesq-sphere)

---

The model equations are

![governing equations](http://mathurl.com/y8cynx9e.png)

with the parameters defined as

![parameters](http://mathurl.com/y7wvyflo.png)

With a homogeneous heat source distribution ![S](http://mathurl.com/ycuc5gxo.png), the background state is

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\Theta_{bg}&space;=&space;\frac{1}{2}\beta\left(1-r^2&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\Theta_{bg}&space;=&space;\frac{1}{2}\beta\left(1-r^2&space;\right&space;)" title="\Theta_{bg} = \frac{1}{2}\beta\left(1-r^2 \right )" /></a>

The system is solved using a Toroidal/Poloidal decomposition of the velocity ![v](http://mathurl.com/y93memaj.png):

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\mathbf{u}=\mathbf{\nabla}\times&space;T&space;\mathbf{r}&space;&plus;&space;\mathbf{\nabla}\times\mathbf{\nabla}\times&space;P&space;\mathbf{r}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\mathbf{u}=\mathbf{\nabla}\times&space;T&space;\mathbf{r}&space;&plus;&space;\mathbf{\nabla}\times\mathbf{\nabla}\times&space;P&space;\mathbf{r}" title="\mathbf{u}=\mathbf{\nabla}\times T \mathbf{r} + \mathbf{\nabla}\times\mathbf{\nabla}\times P \mathbf{r}" /></a>

Note that the Toroidal and Poloidal equations are multiplied by the inverse horizontal laplacian.

---

back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[sphere](models-boussinesq-sphere)
