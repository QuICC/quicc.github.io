back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[plane](models-boussinesq-plane)

---
The model equations are
```math
\begin{aligned}
d_t \nabla^2_{\bot} \Psi + J[\Psi ,  \nabla^2_{\bot} \Psi]- \partial_Z W = \mathbf{B} \cdot \nabla_{\bot} (\partial_x b_y' - \partial_y b_x') +  \nabla^4_{\bot} \Psi \\
d_t W + J[W, \nabla^2_{\bot} \Psi] + \partial_Z \Psi = \frac{\tilde{Ra}}{Pr} \theta + \mathbf{B} \cdot \nabla_{\bot} b_z' + \nabla^2_{\bot} W \\
d_t \theta + J[\theta, \nabla^2_{\bot} \Psi] +  W\partial_Z \overline{\Theta}   = \frac{1}{Pr}  \nabla^2_{\bot} \theta \\
\partial_\tau \overline{\Theta}  +  \partial_Z\left ( \overline{W\theta}\right ) = \frac{1}{Pr} \partial_{ZZ}  \overline{\Theta}\\
\partial_{\tau} B_x = -\partial_Z \overline{E}_y + \frac{1}{\tilde{Pm}} \partial_{ZZ} Bx \\
\partial_{\tau} B_y = \partial_Z \overline{E}_x + \frac{1}{\tilde{Pm}} \partial_{ZZ} By \\
0 = \mathbf{B} \cdot \nabla_{\bot} \mathbf{u}' + \frac{1}{\tilde{Pm}} \nabla^2_{\bot} \mathbf{b}'  
\end{aligned}
```
Here
```math
\begin{aligned}
\overline{E}_y = \overline{(wb_x' - ub_z')}  = \overline{(wb_x' + \partial_y \Psi b_z')}  \, , \qquad \overline{E}_x = \overline{(vb_z' - wb_y')} = \overline{(\partial_x \Psi b_z' - wb_y')}
\end{aligned}
```
The average on these equations is always horizontal but can be average in time (using IScalarTimeAveragedEquation for the EMFx, EMFy equation files)

The last equation is used to solve for 
```math
\begin{aligned}
b_x' = -\tilde{Pm} \nabla^{-2}_{\bot}(B_x \partial_x u + B_y \partial_y u) =  \tilde{Pm} \nabla^{-2}_{\bot}(B_x \partial_{xy} \Psi + B_y \partial_{yy} \Psi)\\
b_y' = -\tilde{Pm} \nabla^{-2}_{\bot}(B_x \partial_x v + B_y \partial_y v) =  -\tilde{Pm} \nabla^{-2}_{\bot}(B_x \partial_{xx} \Psi + B_y \partial_{yx} \Psi)\\
b_z' = -\tilde{Pm} \nabla^{-2}_{\bot}(B_x \partial_x w + B_y \partial_y w)
\end{aligned}
```
---

back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[plane](models-boussinesq-plane)
