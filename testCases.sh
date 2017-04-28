echo "beginning testing"
echo "testing Driver.py with InvalidDirectionTest.txt"
python code/Driver.py < code/tests/InvalidDirectionTest.txt
echo "testing Driver.py with InvalidInputTest.txt"
python code/Driver.py < code/tests/InvalidInputTest.txt
echo "testing Driver.py with LoadTest.txt - expecting no file found"
python code/Driver.py < code/tests/LoadTest.txt
echo "testing Driver.py with SaveTest.txt"
python code/Driver.py < code/tests/SaveTest.txt
echo "testing Driver.py with MapSpanTest.txt"
python code/Driver.py < code/tests/MapSpanTest.txt
echo "done testing"
