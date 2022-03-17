
class Resources:
    d_1 = {}
    d_2 = {}
    d_3 = {}

    d_1_stats = {}
    d_2_stats = {}
    d_3_stats = {}

    @classmethod
    def update_stats(cls):
        for i, d in enumerate((cls.d_1, cls.d_2, cls.d_3), start=1):
            total = sum(d.values())
            for key, value in d.items():
                getattr(cls, f'd_{i}_stats').update({key: value / total})

    @classmethod
    def clear_resources(cls):
        cls.d_1.clear()
        cls.d_2.clear()
        cls.d_3.clear()

        cls.d_1_stats.clear()
        cls.d_2_stats.clear()
        cls.d_3_stats.clear()

