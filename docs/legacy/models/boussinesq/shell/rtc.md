back to [home](/)/[legacy](/legacy)/[models](/legacy/models)/[boussinesq](/legacy/models/boussinesq)/[shell](/legacy/models/boussinesq/shell)

---

The model equations are
```math
\begin{aligned}
\left(\partial_t - \Delta\right)\bold{u} &= \bold{u}\times\left(\nabla\times\bold{u}\right) + \frac{Ra}{E}\Theta\bold{r} - \frac{1}{E}\hat{\bold{z}}\times\bold{u} - \nabla\Pi\\\\
\left(\partial_t - \frac{1}{Pr}\Delta\right)\Theta & = \frac{S}{Pr} - \bold{u}\cdot\nabla\Theta\\\\
\nabla\cdot\bold{u} & =0
\end{aligned}
```

with the parameters defined as
```math
\begin{aligned}
E & = \frac{\nu}{2\Omega d^2}\\\\
Pr &= \frac{\nu}{\kappa}\\\\
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

Note that the Toroidal and Poloidal equations are multiplied by the inverse horizontal laplacian.

---

back to [home](/)/[legacy](/legacy)/[models](/legacy/models)/[boussinesq](/legacy/models/boussinesq)/[shell](/legacy/models/boussinesq/shell)
