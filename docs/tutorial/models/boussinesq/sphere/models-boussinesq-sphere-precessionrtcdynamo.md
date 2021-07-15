back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[sphere](models-boussinesq-sphere)

---

The model equations are

![governing equations]()
```math
\begin{aligned}
\left(\partial_t - E\Delta\right)\bold{u} &= \bold{u}\times\left(\nabla\times\bold{u}\right) + \left(\nabla\times\bold{B}\right)\times\bold{B} + \frac{Ra E}{Pr}\Theta\bold{r} - 2\left(\hat{\bold{z}} + P_o\hat{\bold{z}}_p\right)\times\bold{u} - P_o\left(\hat{\bold{z}}_p\times\hat{\bold{z}}\right)\times\bold{r} - \nabla\Pi\\\\
\left(\partial_t - \frac{E}{Pm}\Delta\right)\bold{B} & = \nabla\times\left(\bold{u}\times\bold{B}\right)\\\\
\left(\partial_t - \frac{E}{Pr}\Delta\right)\Theta & = \frac{E}{Pr}S - \bold{u}\cdot\nabla\Theta\\\\
\nabla\cdot\bold{u} & =0\\\\
\nabla\cdot\bold{B} & = 0
\end{aligned}
```

with the parameters defined as

![parameters]()
```math
\begin{aligned}
E &= \frac{\nu}{\Omega r_o^2}\\\\
Po & = \frac{\Omega_p}{\Omega}\\\\
Pr &= \frac{\nu}{\kappa}\\\\
Pm &= \frac{\nu}{\eta}\\\\
Ra &= \frac{g\alpha\beta r_o^3}{\Omega\kappa}
\end{aligned}
```

With a homogeneous heat source distribution ![S](http://mathurl.com/ycuc5gxo.png), the background state is

![background](http://mathurl.com/y7y6zu5x.png)

The system is solved using a Toroidal/Poloidal decomposition of the velocity ![v](http://mathurl.com/y93memaj.png):

![toroidal/poloidal velocity](http://mathurl.com/y8dxqwtn.png)

and for the magnetic field ![B](http://mathurl.com/yaoe43xc.png):

![toroidal/poloidal magnetic](http://mathurl.com/ya925ysc.png)

Note that the Toroidal and Poloidal equations are multiplied by the inverse horizontal laplacian.

---

back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[sphere](models-boussinesq-sphere)
