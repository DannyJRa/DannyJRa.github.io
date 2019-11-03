# Extend from any of the workspace versions/flavors
# Using latest as version is not recommended, please specify a specific version
FROM mltooling/ml-workspace:latest

# Run you customizations, e.g.
RUN jupyter nbextension enable zenmode/main

 # Install r-runtime, r-kernel, and r-studio web server from provided install scripts
#RUN /bin/bash $RESOURCES_PATH/tools/r-runtime.sh --install && \
#    /bin/bash $RESOURCES_PATH/tools/r-studio-server.sh --install && \
    # Cleanup Layer - removes unneccessary cache files
#    clean-layer.sh