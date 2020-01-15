import pytest

from jmeter_api.non_test_elements.test_plan.elements import TestPlan
from jmeter_api.basics.pre_processor.elements import BasicPreProcessor
from jmeter_api.basics.post_processor.elements import BasicPostProcessor
from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.assertion.elements import BasicAssertion
from jmeter_api.basics.listener.elements import BasicListener
from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.timer.elements import BasicTimer
from jmeter_api.basics.thread_group.elements import BasicThreadGroup
from jmeter_api.basics.test_fragment.elements import BasicTestFragment
from jmeter_api.basics.utils import tag_wrapper


class TestTestPlanArgs:
    # name type check
    class TestContinueForever:
        def test_check(self):
            with pytest.raises(TypeError):
                TestPlan(functional_mode="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                TestPlan(functional_mode="123")

        def test_positive(self):
            TestPlan(functional_mode=True)

    class TestContinueForever:
        def test_check(self):
            with pytest.raises(TypeError):
                TestPlan(teardown_on_shutdown="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                TestPlan(teardown_on_shutdown="123")

        def test_positive(self):
            TestPlan(teardown_on_shutdown=False)

    class TestContinueForever:
        def test_check(self):
            with pytest.raises(TypeError):
                TestPlan(serialize_threadgroups="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                TestPlan(serialize_threadgroups="123")

        def test_positive(self):
            TestPlan(serialize_threadgroups=True)

class TestTestPlanAppend:
    def test_negative1(self):
        with pytest.raises(TypeError):
            TestPlan().append(BasicSampler())
    def test_negative2(self):
        with pytest.raises(TypeError):
            TestPlan().append(BasicController())
    def test_negative3(self):
        with pytest.raises(TypeError):
            TestPlan().append(TestPlan())

    def test_positive1(self):
        TestPlan().append(BasicPreProcessor())
    def test_positive2(self):
        TestPlan().append(BasicPostProcessor())
    def test_positive3(self):
        TestPlan().append(BasicThreadGroup())
    def test_positive4(self):
        TestPlan().append(BasicConfig())
    def test_positive5(self):
        TestPlan().append(BasicTestFragment())
    def test_positive6(self):
        TestPlan().append(BasicAssertion())
    def test_positive7(self):
        TestPlan().append(BasicListener())
    def test_positive8(self):
        TestPlan().append(BasicTimer())
