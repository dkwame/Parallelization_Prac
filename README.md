# Parallelization_Prac

 This project is simply a quick exercise in parallelizing different processes in order to speed up computation time. 
It is noted at with smaller computations parallelization benefits are negligible, however, as processes become more complex, it becomes important to calculate simultaneously rather than serially. 
  E.G. in the trapezoidal approximation problem compare the computation times when three trapezoids are used to approximate and then three thousand trapezoids. Computation times are generally lower than when serially performed. 

It is also important to note that increasing parallelization arbitrarily does not necessarily improve computation times. Per Amdahl’s Law  “the overall performance improvement gained by optimizing a single part of a system is limited by the fraction of time that the improved part is actually used”.  In fact, adding too many processors arbitrarily could slow computation times. As you will see, gauging available processors or nodes and determining usefulness is vital in parallelization. 

Check my Iris classification notebook for applications of parallelization on machine learning algorithms and how that affects speed. 
