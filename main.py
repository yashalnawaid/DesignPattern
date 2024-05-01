# Command Pattern
class Command:
    def execute(self):
        pass

class BuildCommand(Command):
    def execute(self):
        print("Executing build steps...")

class TestCommand(Command):
    def execute(self):
        print("Executing test steps...")

class DeployCommand(Command):
    def execute(self):
        print("Executing deploy steps...")

# Decorator Pattern
class PipelineStep:
    def execute(self):
        pass

class BuildStep(PipelineStep):
    def execute(self):
        print("Executing build steps...")

class TestStep(PipelineStep):
    def execute(self):
        print("Executing test steps...")

class AdditionalFeatureDecorator(PipelineStep):
    def __init__(self, pipeline_step):
        self._pipeline_step = pipeline_step

    def execute(self):
        self._pipeline_step.execute()
        print("Additional functionality added...")

# State Pattern
class PipelineState:
    def execute(self):
        pass

class RunningState(PipelineState):
    def execute(self):
        print("Pipeline is running...")

class PausedState(PipelineState):
    def execute(self):
        print("Pipeline is paused...")

class PipelineContext:
    def __init__(self, state):
        self._state = state

    def change_state(self, state):
        self._state = state

    def execute_pipeline(self):
        self._state.execute()

# Factory Pattern
class PipelineFactory:
    def create_pipeline(self):
        pass

class BasicPipeline(PipelineFactory):
    def create_pipeline(self):
        return BuildStep()

class AdvancedPipeline(PipelineFactory):
    def create_pipeline(self):
        return AdditionalFeatureDecorator(TestStep())

# Usage
if __name__ == "__main__":
    # Command Pattern
    print("--- Command Pattern ---")
    build_cmd = BuildCommand()
    test_cmd = TestCommand()
    deploy_cmd = DeployCommand()

    build_cmd.execute()
    test_cmd.execute()
    deploy_cmd.execute()

    # Decorator Pattern
    print("\n--- Decorator Pattern ---")
    basic_pipeline = BuildStep()
    basic_pipeline.execute()

    advanced_pipeline = AdditionalFeatureDecorator(TestStep())
    advanced_pipeline.execute()

    # State Pattern
    print("\n--- State Pattern ---")
    running_state = RunningState()
    paused_state = PausedState()

    context = PipelineContext(running_state)
    context.execute_pipeline()

    context.change_state(paused_state)
    context.execute_pipeline()

    # Factory Pattern
    print("\n--- Factory Pattern ---")
    factory = BasicPipeline()
    pipeline = factory.create_pipeline()
    pipeline.execute()

    factory = AdvancedPipeline()
    pipeline = factory.create_pipeline()
    pipeline.execute()

