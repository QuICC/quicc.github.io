back to [home](/)/[legacy](/legacy)/[models](/legacy/models)/[boussinesq](/legacy/models/boussinesq)/[shell](/legacy/models/boussinesq/shell)

---

The model equations are
```math
\begin{aligned}
\left(\partial_t - \Delta\right)\bold{u} &= \bold{u}\times\left(\nabla\times\bold{u}\right) - \frac{1}{E}\hat{\bold{z}}\times\bold{u} - \nabla\Pi\\\\
\nabla\cdot\bold{u} & =0
\end{aligned}
```

with the parameters defined as
```math
\begin{aligned}
E & = \frac{\nu}{2\Omega d^2}\\\\
\end{aligned}
```

The system is solved using a Toroidal/Poloidal decomposition of the velocity $`\bold{u}`$:
```math
\bold{u} = \nabla\times T\bold{r} + \nabla\times\nabla\times P\bold{r}
```

Note that the Toroidal and Poloidal equations are multiplied by the inverse horizontal laplacian.

---

back to [home](/)/[legacy](/legacy)/[models](/legacy/models)/[boussinesq](/legacy/models/boussinesq)/[shell](/legacy/models/boussinesq/shell)
