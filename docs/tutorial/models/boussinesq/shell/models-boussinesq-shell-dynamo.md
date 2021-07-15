back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[shell](models-boussinesq-shell)

---

The model equations are
```math
\begin{aligned}
\left(E_m\partial_t - E\Delta\right)\bold{u} &= E_m\bold{u}\times\left(\nabla\times\bold{u}\right) + \left(\nabla\times\bold{B}\right)\times\bold{B} + q Ra\Theta\bold{r} - \hat{\bold{z}}\times\bold{u} - \nabla\Pi\\\\
\left(\partial_t - \Delta\right)\bold{B} & = \nabla\times\left(\bold{u}\times\bold{B}\right)\\\\
\left(\partial_t - q\Delta\right)\Theta & = S - \bold{u}\cdot\nabla\Theta\\\\
\nabla\cdot\bold{u} & =0\\\\
\nabla\cdot\bold{B} & = 0
\end{aligned}
```

with the parameters defined as
```math
\begin{aligned}
E &= \frac{\nu}{2\Omega d^2}\\\\
E_m &= \frac{\eta}{2\Omega d^2}\\\\
q &= \frac{\kappa}{\eta}\\\\
Ra &= \frac{g\alpha\beta d^3}{2\Omega\kappa}
\end{aligned}
```

With a homogeneous heat source distribution $`S = 3`$, the background state is
```math
\Theta_{bg} = - \frac{T_i - T_o}{r_o^2 - r_i^2}r^2 + \frac{r_o^2 T_i - r_i^2 T_o}{r_o^2 - r_i^2}
```
and for differential heating
```math
\Theta_{bg} = \frac{r_i r_o\left(T_i - T_o\right)}{r_o - r_i}\frac{1}{r} + \frac{T_o r_o - T_i r_i}{r_o - r_i}
```

The system is solved using a Toroidal/Poloidal decomposition of the velocity $`\bold{u}`$:
```math
\bold{u} = \nabla\times T\bold{r} + \nabla\times\nabla\times P\bold{r}
```
and for the magnetic field $`\bold{B}`$:
```math
\bold{B} = \nabla\times \mathcal{T}\bold{r} + \nabla\times\nabla\times \mathcal{P}\bold{r}
```

Note that the Toroidal and Poloidal equations are multiplied by the inverse horizontal laplacian.

---

back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[shell](models-boussinesq-shell)
