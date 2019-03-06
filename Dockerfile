FROM redmine:4.0

ENTRYPOINT ["/docker-entrypoint.sh"]

RUN cd public/themes && \
  # Install the PurpleMine2 theme
  wget --continue https://github.com/mrliptontea/PurpleMine2/archive/v1.9.0.tar.gz && \
  tar xvfz v1.9.0.tar.gz && rm -f v1.9.0.tar.gz && \
  # Install the YeniHayat theme
  wget --continue https://github.com/yenihayat/redmine-theme-yh/archive/1.6.tar.gz && \
  tar xvfz 1.6.tar.gz && rm -f 1.6.tar.gz && \
  # Install
  wget --continue https://github.com/Nitrino/flatly_light_redmine/archive/v0.2.3.tar.gz && \
  tar xvfz v0.2.3.tar.gz && rm -f v0.2.3.tar.gz

EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]
