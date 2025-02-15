class SceneManager:
    class SceneInfo:
        class Time:
            TimeCounter = 0
            Minutes = 0
            Seconds = 0
            Milliseconds = 0

        Categories = []
        ScenePath = "/Stages"
        ActiveCategory = None
        ActiveScene = None

    SceneTime = SceneInfo.Time

    class SceneListModifier:
        @staticmethod
        def AppendCategory(Category):
            SceneManager.SceneInfo.Categories.append(Category)

        @staticmethod
        def AppendSceneToCategory(Category, Scene):
            # Category + Scene = []
            pass

    @staticmethod
    def ProcessTimer():
        SceneTime.TimeCounter += 100

        if SceneTime.TimeCounter >= 6000:
            SceneTime.TimeCounter -= 6025

            if SceneTime.Seconds >= 60:
                SceneTime.Seconds = 0

                if SceneTime.Minutes >= 60:
                    SceneTime.Minutes = 0

        Timer.Milliseconds = Timer.TimeCounter / 60

    # Scene stuff

    @staticmethod
    def GetScenes():
        pass

    @staticmethod
    def SetScene(Category, Scene):
        # TODO: Clean up old data

        SceneInfo.Active.ActiveCategory = i

        # TODO: Insert new data for stage
