from django.conf.urls.defaults import patterns, include, handler500, handler404

urlpatterns = patterns('tardis.apps.mrtardis.views',
                       (r'^index/(?P<experiment_id>\d+)/$',
                        'index'),
                       (r'^test_user_setup/(?P<experiment_id>\d+)/$',
                        'test_user_setup'),
                       (r'^MRform/(?P<experiment_id>\d+)/$',
                        'MRform'),
                       (r'^parForm/(?P<dataset_id>\d+)/$',
                        'parForm'),
                       (r'^displayResults/(?P<experiment_id>\d+)/$',
                        'displayResults'),
                       (r'^type_filtered_file_list/(?P<dataset_id>\d+)/$',
                        'type_filtered_file_list'),
                       (r'^add_pdb_files/(?P<dataset_id>\d+)/$',
                        'add_pdb_files'),
                       (r'^parseMTZfile/(?P<dataset_id>\d+)/$',
                        'parseMTZfile'),
                       (r'^runMR/(?P<dataset_id>\d+)/$',
                        'runMR'),
                       (r'^deleteFile/(?P<dataset_id>\d+)/$',
                        'deleteFile'),
                       (r'^jobfinished/(?P<dataset_id>\d+)/$',
                        'jobfinished'),
                       )