<h1>Python implementation of the Open MP</h2>
<p>
This is the python project, done as a part of Parallel Computing Course.
</p>
<h2>OpenMP</h2>
<hr/>
<p>
OpenMP (Open Multi-Processing) is an API that supports multi-platform shared memory multiprocessing programming in C,
C++, and Fortran, on most processor architectures and operating systems, including Solaris, AIX, HP-UX, GNU/Linux,
Mac OS X, and Windows platforms. 

It consists of a set of compiler directives, library routines, and environment variables 
that influence run-time behavior.
</p>

<h2>PyOpenMP</h2>
<hr/>
<p>
The project is about the implementation of the OpenMP Application Programming Interface for Python. 
OpenMP enables the programmer to extend the sequentialprogramming model, to enable parallelism by providing
various Single Instruction Multiple Data(SIMD) constructs, synchronisation and the work sharing constructs. It also
enables the sharing and privatisation of the variables.

PyOpenMP is an attempt to enable developers using Python, to achieve parallelism in a simple manner.
Decorators and the multiprocessing module of python are used to achieve this.The project attempts to provide 
various constructs like <h3>@OMPParallel</h3> and <h3>@OMPFor</h3> for the creation of multiple processes to 
execute a piece of Python code. It also attempts to provide various synchronisation directives like <h2>@OMPMaster</h2>
and <h2>@OMPSingle</h2> and various data sharing attribute clauses like private, ﬁrstprivate, and shared.
</p>

<h4>Implementation provided for </h4>
<hr/>
  <ul>
				   <li> parallel directive - <h3>OMPParallel</h3></li>
					 <li> for directive - <h3>OMPFor</h3></li>
					 <li> single directive - <h3>OMPSingle</h3></li>
					 <li> master directive - <h3>OMPMaster</h3></li>
					 <li> clauses - <h3>private, firstprivate, shared (partial)</h3></li>
	</ul>
<h2> directives explained </h2>
<ul>
  <li>OMPParallel
    <ul>
      <li>
        This class models every process. Since “multiprocessing” module is used thread is 
        mapped to a process in the implementation. Thus this class is analogous to the thread
        module.
      </li>
    </ul>
  </li>
  <li>OMPFor
    <ul>
      <li>
        This is a decorator class which is used to decorate the function which contains a for loop
        and has to be parallelised. Once the @OMPFor is encountered the team of threads divide 
        the for loop among them to execute them in parallel.
      </li>
    </ul>
  </li>
  <li>OMPMaster
    <ul>
      <li>
        This is a decorator a class which is used to decorate the function that needs to be executed 
        only by the master process. All the other processes continue execution without waiting.
        There is no barrier implied for a for construct.
      </li>
    </ul>
  </li>
  <li>OMPSingle
    <ul>
      <li>
        This is a decorator class which is used to decorate the function that needs to be executed
        by any one process not necessarily the master process. An implicit barrier is implied 
        which makes sure that the other processes wait until the execution of the single function is 
        complete.
      </li>
    </ul>
  </li>
</ul>
<h2> External libraries used </h2>
<hr/>
<ul>
  <li><a href="http://docs.python.org/2/library/multiprocessing.html">multiprocessing</a></li>
</ul>
  
