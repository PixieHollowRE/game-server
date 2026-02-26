COMMUNITY_ALERTS_ALL = 3

OTP_DO_ID_FAIRIES_BADGE_MANAGER = 4690

# Everything from this zone up to the top of the available range is
# reserved for the dynamic zone pool.  Note that our effective maximum
# zone may be less than DynamicZonesEnd, depending on the assignment
# of available doIds--we must be careful not to overlap.
DynamicZonesBegin =    61000
DynamicZonesEnd =      (1 << 20)
