from pysnptools.pstreader import PstNpz
from pysnptools.kernelreader import KernelReader
import logging


class KernelNpz(KernelReader,PstNpz):
    '''
    A :class:`.KernelReader` for reading \*.kernel.npz files from disk.

    See :class:`.KernelReader` for general examples of using KernelReaders.

    The general NPZ format is described in http://docs.scipy.org/doc/numpy/reference/generated/numpy.savez.html. The KernelNpz format stores
    val, iid0, and iid1 information in NPZ format.
   
    **Constructor:**
        :Parameters: * **filename** (*string*) -- The KernelNpz file to read.

        :Example:

        >>> from pysnptools.kernelreader import KernelNpz
        >>> data_on_disk = KernelNpz('../examples/toydata.kernel.npz')
        >>> print data_on_disk.iid_count
        500

    **Methods beyond** :class:`.KernelReader`

    '''

    def __init__(self,*args, **kwargs):
        super(KernelNpz, self).__init__(*args, **kwargs)

    @staticmethod
    def write(filename, kerneldata):
        """Writes a :class:`KernelData` to KernelNpz format.

        :param filename: the name of the file to create
        :type filename: string
        :param kerneldata: The in-memory data that should be written to disk.
        :type kerneldata: :class:`KernelData`

        >>> from pysnptools.snpreader import Bed
        >>> from pysnptools.standardizer import Unit
        >>> import pysnptools.util as pstutil
        >>> kerneldata = Bed('../examples/toydata.bed',count_A1=False).read_kernel(Unit())     # Create a kernel from the data in the Bed file
        >>> pstutil.create_directory_if_necessary("tempdir/toydata.kernel.npz")
        >>> KernelNpz.write("tempdir/toydata.kernel.npz",kerneldata)      # Write data in KernelNpz format
        """
        PstNpz.write(filename,kerneldata)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    import doctest
    doctest.testmod()
