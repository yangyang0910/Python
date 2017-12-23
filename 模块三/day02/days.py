class ABC:
    def __init__(self):
        print("SS")

    def __call__(self, *args, **kwargs):
        print(args)

ABC()("sdas","dasda")
