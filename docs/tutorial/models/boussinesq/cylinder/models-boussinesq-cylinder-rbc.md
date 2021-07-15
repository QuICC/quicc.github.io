back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[cylinder](models-boussinesq-cylinder)

---

The model equations are
```math
\begin{aligned}
\left(\partial_t - \Delta\right)\bold{u} &=  \bold{u}\times\left(\nabla\times\bold{u}\right) + Ra\Theta\hat{\bold{z}} - \nabla\Pi\\\\
\left(\partial_t - \frac{1}{Pr}\Delta\right)\Theta & = - \bold{u}\cdot\nabla\Theta\\\\
\nabla\cdot\bold{u} & =0
\end{aligned}
```

with the parameters defined as
```math
\begin{aligned}
Pr &= \frac{\nu}{\kappa}\\\\
Ra &= \frac{g\alpha\Delta T d^3}{\nu\kappa}
\end{aligned}
```

By imposing a constant hot bottom lid and cold top lid, the background state is given by
```math
\Theta_{bg} =1-z
```

The system is solved using a Toroidal/Poloidal decomposition of the velocity $`\bold{u}`$:
```math
\bold{u} = \nabla\times \psi\hat{\bold{z}} + \nabla\times\nabla\times \phi\hat{\bold{z}}
```

The Toroidal/Poloidal model equations are given by
```math
\begin{aligned}
\left(\partial_t - \Delta\right)\Delta_h\psi &= \hat{\bold{e}_z}\cdot\nabla\times\left(\bold{u}\cdot\nabla\right)\bold{u}\\\\
\left(\partial_t - \Delta\right)\Delta\Delta_h\phi &= -Ra \Delta_h\Theta - \hat{\bold{e}_z}\cdot\nabla\times\nabla\times\left(\bold{u}\cdot\nabla\right)\bold{u}\\\\
\left(\partial_t - \frac{1}{Pr}\Delta\right)\Theta &= -\bold{u}\cdot\nabla\Theta
\end{aligned}
```

---

back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[cylinder](models-boussinesq-cylinder)
