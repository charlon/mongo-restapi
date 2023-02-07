if [ "$ENV"  = "localdev" ]

  # create sh script to load initial data into mongo
  python3 manage.py create_collections

then
  . /scripts/app_deploy.sh
fi
