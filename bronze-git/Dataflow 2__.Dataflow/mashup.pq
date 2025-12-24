[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
shared a_final_common_table = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "02388c9c-dc85-46bb-9eaf-4b3762849643"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "0d0eff1a-c9a2-465c-9cda-68f170e346f6"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "a_final_common_table", ItemKind = "Table"]}[Data]
in
  #"Navigation 2";
