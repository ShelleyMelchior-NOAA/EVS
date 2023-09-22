#!/usr/bin/env python3
# =============================================================================
#
# NAME: cam_plots_snowfall_graphx_defs.py
# CONTRIBUTOR(S): Marcel Caron, marcel.caron@noaa.gov, NOAA/NWS/NCEP/EMC-VPPPGB
# PURPOSE: Graphics definitions for the CAM Snowfall Plots jobs
#
# =============================================================================

import os
from datetime import datetime, timedelta as td
graphics = {
    'cam':{
        'snowfall':{
            'nohrsc':{
                'namnest, hireswarw, hireswarwmem2, hireswfv3, hrrr':{
                    'threshold_average':{
                        'DATE_TYPE':'INIT',
                        'VALID_BEG':'',
                        'VALID_END':'',
                        'INIT_BEG':'',
                        'INIT_END':'',
                        'VX_MASK_LIST':'CONUS,CONUS_East,CONUS_West,CONUS_Central,CONUS_South',
                        'EVAL_PERIODS':['LAST31DAYS','LAST90DAYS'],
                        'VARIABLES':{
                            'ctc':{
                                'WEASD_06':{
                                    'FCST_VALID_HOURS':[''],
                                    'FCST_INIT_HOURS':['0','12'],
                                    'STATSs':['fbias','ets'],
                                    'FCST_LEADS':['24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48','36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60'],
                                    'FCST_LEVEL':'Z0',
                                    'OBS_LEVEL':'A06',
                                    'FCST_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'OBS_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'CONFIDENCE_INTERVALS':'False',
                                    'INTERP':'NEAREST',
                                    'INTERP_PNTSs':[''],
                                },
                                'SNOD_06':{
                                    'FCST_VALID_HOURS':[''],
                                    'FCST_INIT_HOURS':['0','12'],
                                    'STATSs':['fbias','ets'],
                                    'FCST_LEADS':['24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48','36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60'],
                                    'FCST_LEVEL':'Z0',
                                    'OBS_LEVEL':'A06',
                                    'FCST_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'OBS_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'CONFIDENCE_INTERVALS':'False',
                                    'INTERP':'NEAREST',
                                    'INTERP_PNTSs':[''],
                                },
                                'WEASD_24':{
                                    'FCST_VALID_HOURS':[''],
                                    'FCST_INIT_HOURS':['0','6','12','18'],
                                    'STATSs':['fbias','ets'],
                                    'FCST_LEADS':['24','30','36','42','48','54','60'],
                                    'FCST_LEVEL':'Z0',
                                    'OBS_LEVEL':'A24',
                                    'FCST_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'OBS_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'CONFIDENCE_INTERVALS':'False',
                                    'INTERP':'NEAREST',
                                    'INTERP_PNTSs':[''],
                                },
                                'SNOD_24':{
                                    'FCST_VALID_HOURS':[''],
                                    'FCST_INIT_HOURS':['0','6','12','18'],
                                    'STATSs':['fbias','ets'],
                                    'FCST_LEADS':['24','30','36','42','48','54','60'],
                                    'FCST_LEVEL':'Z0',
                                    'OBS_LEVEL':'A24',
                                    'FCST_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'OBS_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'CONFIDENCE_INTERVALS':'False',
                                    'INTERP':'NEAREST',
                                    'INTERP_PNTSs':[''],
                                },
                            },
                            'nbrcnt':{
                                'WEASD_06':{
                                    'FCST_VALID_HOURS':[''],
                                    'FCST_INIT_HOURS':['0','12'],
                                    'STATSs':['fss'],
                                    'FCST_LEADS':['24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48','36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60'],
                                    'FCST_LEVEL':'Z0',
                                    'OBS_LEVEL':'A06',
                                    'FCST_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'OBS_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'CONFIDENCE_INTERVALS':'False',
                                    'INTERP':'NBRHD_SQUARE',
                                    'INTERP_PNTSs':['1','25','81','441','961','3969'],
                                },
                                'SNOD_06':{
                                    'FCST_VALID_HOURS':[''],
                                    'FCST_INIT_HOURS':['0','12'],
                                    'STATSs':['fss'],
                                    'FCST_LEADS':['24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48','36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60'],
                                    'FCST_LEVEL':'Z0',
                                    'OBS_LEVEL':'A06',
                                    'FCST_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'OBS_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'CONFIDENCE_INTERVALS':'False',
                                    'INTERP':'NBRHD_SQUARE',
                                    'INTERP_PNTSs':['1','25','81','441','961','3969'],
                                },
                                'WEASD_24':{
                                    'FCST_VALID_HOURS':[''],
                                    'FCST_INIT_HOURS':['0','6','12','18'],
                                    'STATSs':['fss'],
                                    'FCST_LEADS':['24','30','36','42','48','54','60'],
                                    'FCST_LEVEL':'Z0',
                                    'OBS_LEVEL':'A24',
                                    'FCST_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'OBS_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'CONFIDENCE_INTERVALS':'False',
                                    'INTERP':'NBRHD_SQUARE',
                                    'INTERP_PNTSs':['1','25','81','441','961','3969'],
                                },
                                'SNOD_24':{
                                    'FCST_VALID_HOURS':[''],
                                    'FCST_INIT_HOURS':['0','6','12','18'],
                                    'STATSs':['fss'],
                                    'FCST_LEADS':['24','30','36','42','48','54','60'],
                                    'FCST_LEVEL':'Z0',
                                    'OBS_LEVEL':'A24',
                                    'FCST_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'OBS_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'CONFIDENCE_INTERVALS':'False',
                                    'INTERP':'NBRHD_SQUARE',
                                    'INTERP_PNTSs':['1','25','81','441','961','3969'],
                                },
                            },
                        }
                    },
                    'performance_diagram':{
                        'DATE_TYPE':'INIT',
                        'VALID_BEG':'',
                        'VALID_END':'',
                        'INIT_BEG':'',
                        'INIT_END':'',
                        'VX_MASK_LIST':'CONUS,CONUS_East,CONUS_West,CONUS_Central,CONUS_South',
                        'EVAL_PERIODS':['LAST31DAYS','LAST90DAYS'],
                        'VARIABLES':{
                            'ctc':{
                                'WEASD_06':{
                                    'FCST_VALID_HOURS':[''],
                                    'FCST_INIT_HOURS':['0','12'],
                                    'STATSs':['sratio,pod,csi'],
                                    'FCST_LEADS':['24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48','36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60'],
                                    'FCST_LEVEL':'Z0',
                                    'OBS_LEVEL':'A06',
                                    'FCST_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'OBS_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'CONFIDENCE_INTERVALS':'False',
                                    'INTERP':'NEAREST',
                                    'INTERP_PNTSs':[''],
                                },
                                'SNOD_06':{
                                    'FCST_VALID_HOURS':[''],
                                    'FCST_INIT_HOURS':['0','12'],
                                    'STATSs':['sratio,pod,csi'],
                                    'FCST_LEADS':['24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48','36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60'],
                                    'FCST_LEVEL':'Z0',
                                    'OBS_LEVEL':'A06',
                                    'FCST_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'OBS_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'CONFIDENCE_INTERVALS':'False',
                                    'INTERP':'NEAREST',
                                    'INTERP_PNTSs':[''],
                                },
                                'WEASD_24':{
                                    'FCST_VALID_HOURS':[''],
                                    'FCST_INIT_HOURS':['0','6','12','18'],
                                    'STATSs':['sratio,pod,csi'],
                                    'FCST_LEADS':['24','30','36','42','48','54','60'],
                                    'FCST_LEVEL':'Z0',
                                    'OBS_LEVEL':'A24',
                                    'FCST_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'OBS_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'CONFIDENCE_INTERVALS':'False',
                                    'INTERP':'NEAREST',
                                    'INTERP_PNTSs':[''],
                                },
                                'SNOD_24':{
                                    'FCST_VALID_HOURS':[''],
                                    'FCST_INIT_HOURS':['0','6','12','18'],
                                    'STATSs':['sratio,pod,csi'],
                                    'FCST_LEADS':['24','30','36','42','48','54','60'],
                                    'FCST_LEVEL':'Z0',
                                    'OBS_LEVEL':'A24',
                                    'FCST_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'OBS_THRESHs':['>=0.0254,>=0.0508,>=0.1016,>=0.2032,>=0.3048'],
                                    'CONFIDENCE_INTERVALS':'False',
                                    'INTERP':'NEAREST',
                                    'INTERP_PNTSs':[''],
                                },
                            }
                        }
                    },
                }
            },
        },
    }
}
