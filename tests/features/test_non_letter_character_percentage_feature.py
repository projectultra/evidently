import pandas as pd

from evidently import ColumnMapping
from evidently.features.non_letter_character_percentage_feature import NonLetterCharacterPercentage
from evidently.utils.data_preprocessing import create_data_definition


def test_non_letter_character_percentage():
    feature_generator = NonLetterCharacterPercentage("column_1")
    data = pd.DataFrame(dict(column_1=["2Ad <4", "abc ", "144&&?1"]))
    result = feature_generator.generate_feature(
        data=data,
        data_definition=create_data_definition(None, data, ColumnMapping()),
    )
    assert result.equals(pd.DataFrame(dict(column_1=[100 * 3 / 6, 0, 100])))
