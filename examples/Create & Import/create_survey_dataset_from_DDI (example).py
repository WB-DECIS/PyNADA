import pynada as nada
import inspect

nada.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = open("API Key.txt", "r").read()
nada.set_api_key(api_key)

######################################
# create_survey_dataset_from_DDI example
######################################

file = "SURVEY_DATASET_SAMPLE_02.xml"
overwrite = "yes"
repository_id = "central"
access_policy = "open"
published = 1

response = nada.create_survey_dataset_from_DDI(
    file=file,
    overwrite=overwrite,
    repository_id=repository_id,
    access_policy=access_policy,
    # data_remote_url=data_remote_url,
    # rdf=rdf,
    # published=published
)

print(response)

# upload temporary thumbnail
dataset_id = response['survey']['idno']
thumbnail_path = nada.text_to_thumbnail("Survey\nDataset")
nada.upload_thumbnail(dataset_id, thumbnail_path)
