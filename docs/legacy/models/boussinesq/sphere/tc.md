back to [home](/)/[legacy](/legacy)/[models](/legacy/models)/[boussinesq](/legacy/models/boussinesq)/[sphere](/legacy/models/boussinesq/sphere)

---

The model equations are

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\begin{align*}&space;\left(\partial_t&space;-&space;\Delta\right)\mathbf{u}&space;&&space;=&space;\mathbf{u}&space;\times&space;\left(&space;\nabla&space;\times&space;\mathbf{u}\right)&space;&plus;&space;\frac{Ra}{Pr}&space;\Theta&space;\mathbf{r}&space;-&space;\nabla\Pi&space;\\[0.6cm]&space;\left(\partial_t&space;-&space;\frac{1}{Pr}\Delta\right)\Theta&space;&&space;=&space;-&space;\mathbf{u}\cdot\nabla\left(\Theta+\Theta_{bg}\right)\\[0.6cm]&space;\nabla\cdot\mathbf{u}&space;&&space;=&space;0&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\begin{align*}&space;\left(\partial_t&space;-&space;\Delta\right)\mathbf{u}&space;&&space;=&space;\mathbf{u}&space;\times&space;\left(&space;\nabla&space;\times&space;\mathbf{u}\right)&space;&plus;&space;\frac{Ra}{Pr}&space;\Theta&space;\mathbf{r}&space;-&space;\nabla\Pi&space;\\[0.6cm]&space;\left(\partial_t&space;-&space;\frac{1}{Pr}\Delta\right)\Theta&space;&&space;=&space;-&space;\mathbf{u}\cdot\nabla\left(\Theta+\Theta­{bg}\right)\\[0.6cm]&space;\nabla\cdot\mathbf{u}&space;&&space;=&space;0&space;\end{align*}" title="\begin{align*} \left(\partial_t - \Delta\right)\mathbf{u} & = \mathbf{u} \times \left( \nabla \times \mathbf{u}\right) + \frac{Ra}{Pr} \Theta \mathbf{r} - \nabla\Pi \\[0.6cm] \left(\partial_t - \frac{1}{Pr}\Delta\right)\Theta & =  - \mathbf{u}\cdot\nabla\left(\Theta+\Theta­_{bg}\right)\\[0.6cm] \nabla\cdot\mathbf{u} & = 0 \end{align*}" /></a>

with the parameters defined as

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\begin{align*}&space;Pr&space;&&space;=&space;\frac{\nu}{\kappa}\\&space;Ra&space;&&space;=&space;\frac{g&space;\alpha&space;\beta&space;r_o^4}{\nu\kappa}&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\begin{align*}&space;Pr&space;&&space;=&space;\frac{\nu}{\kappa}\\&space;Ra&space;&&space;=&space;\frac{g&space;\alpha&space;\beta&space;r_o^4}{\nu\kappa}&space;\end{align*}" title="\begin{align*} Pr & = \frac{\nu}{\kappa}\\ Ra & = \frac{g \alpha \beta r_o^4}{\nu\kappa} \end{align*}" /></a>

With a homogeneous heat source distribution <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;S=3" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;S=3" title="S=3" /></a>, the background state is

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\Theta_{bg}&space;=&space;\frac{1}{2}\beta\left(1-r^2&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\Theta_{bg}&space;=&space;\frac{1}{2}\beta\left(1-r^2&space;\right&space;)" title="\Theta_{bg} = \frac{1}{2}\beta\left(1-r^2 \right )" /></a>

The system is solved using a Toroidal/Poloidal decomposition of the velocity <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\mathbf{u}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\mathbf{u}" title="\mathbf{u}" /></a>:

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\mathbf{u}=\mathbf{\nabla}\times&space;T&space;\mathbf{r}&space;&plus;&space;\mathbf{\nabla}\times\mathbf{\nabla}\times&space;P&space;\mathbf{r}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\mathbf{u}=\mathbf{\nabla}\times&space;T&space;\mathbf{r}&space;&plus;&space;\mathbf{\nabla}\times\mathbf{\nabla}\times&space;P&space;\mathbf{r}" title="\mathbf{u}=\mathbf{\nabla}\times T \mathbf{r} + \mathbf{\nabla}\times\mathbf{\nabla}\times P \mathbf{r}" /></a>

Note that the Toroidal and Poloidal equations are multiplied by the inverse horizontal laplacian.

---

back to [home](/)/[legacy](/legacy)/[models](/legacy/models)/[boussinesq](/legacy/models/boussinesq)/[sphere](/legacy/models/boussinesq/sphere)
