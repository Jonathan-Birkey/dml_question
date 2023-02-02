import stest
import conf
import dev_util


my_dev = pre_conf_object('my_dev', 'my_device')
SIM_add_configuration([my_dev], None)

# Replace our pre_conf_object reference with
# a reference to the Simics obj
my_dev = conf.my_dev

# Define test
def set_attribute():
    my_dev.myAttribute = [1.1, 1]
    stest.expect_equal(my_dev.myAttribute[0], 1.1)

# Run test code
set_attribute()
